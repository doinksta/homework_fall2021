from cs285.infrastructure import pytorch_util as ptu
from .base_exploration_model import BaseExplorationModel
import torch.optim as optim
from torch import nn
import torch

def init_method_1(model):
    model.weight.data.uniform_()
    model.bias.data.uniform_()

def init_method_2(model):
    model.weight.data.normal_()
    model.bias.data.normal_()

def init_method_3(model):
    model.weight.data.log_normal_()
    model.bias.data.log_normal_()


class CustomModel(nn.Module, BaseExplorationModel):
    def __init__(self, hparams, optimizer_spec, **kwargs):
        super().__init__(**kwargs)
        self.ob_dim = hparams['ob_dim']
        self.output_size = hparams['rnd_output_size']
        self.n_layers = hparams['rnd_n_layers']
        self.size = hparams['rnd_size']
        self.optimizer_spec = optimizer_spec

        # <DONE>: Create two neural networks:
        # 1) f, the random function we are trying to learn
        # 2) f_hat, the function we are using to learn f
        # WARNING: Make sure you use different types of weight
        #          initializations for these two functions

        # HINT 1) Check out the method ptu.build_mlp
        # HINT 2) There are two weight init methods defined above

        self.f = ptu.build_mlp(self.ob_dim, self.output_size, self.n_layers, self.size, init_method=init_method_1)
        self.f_hat = ptu.build_mlp(self.ob_dim, self.output_size, self.n_layers, self.size, init_method=init_method_2)
        self.f_hat2 = ptu.build_mlp(self.ob_dim, self.output_size, self.n_layers, self.size, init_method=init_method_3)

        def _temp():
            import itertools
            for name, param in itertools.chain(self.f_hat.named_parameters(), self.f_hat2.named_parameters()):
                yield param

        self.optimizer = self.optimizer_spec.constructor(
            _temp(),
            **self.optimizer_spec.optim_kwargs
        )

        self.learning_rate_scheduler = optim.lr_scheduler.LambdaLR(
            self.optimizer,
            self.optimizer_spec.learning_rate_schedule,
        )

        self.f.to(ptu.device)
        self.f_hat.to(ptu.device)
        self.f_hat2.to(ptu.device)

    def forward(self, ob_no):
        # <DONE>: Get the prediction error for ob_no
        # HINT: Remember to detach the output of self.f!
        targets = self.f(ob_no).detach()
        predictions = self.f_hat(ob_no)
        predictions2 = self.f_hat2(ob_no)

        norm = torch.norm(predictions - targets, dim=1)[..., None]
        norm2 = torch.norm(predictions2 - targets, dim=1)[..., None]

        return torch.logsumexp(torch.cat([norm, norm2], 1), 1)

    def forward_np(self, ob_no):
        ob_no = ptu.from_numpy(ob_no)
        error = self(ob_no)
        return ptu.to_numpy(error)

    def update(self, ob_no):
        # <DONE>: Update f_hat using ob_no
        # Hint: Take the mean prediction error across the batch
        prediction_errors = self(ptu.from_numpy(ob_no))
        loss = torch.mean(prediction_errors)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()
