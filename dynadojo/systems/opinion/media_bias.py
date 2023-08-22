import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.opinions as op

from ..utils import NetworkSystem

import numpy as np

class MediaBiasSystem(NetworkSystem):
    def __init__(self, latent_dim, embed_dim,
                 noise_scale=0.01,
                 IND_range=(0, 0.5),
                 OOD_range=(0.5, 1),
                 epsilon=0.32,
                 gamma=0,
                 p_edge=1,
                 n_media=3,
                 p_interaction=0.1,
                 gamma_media=0.1,
                 seed=None):

        super().__init__(latent_dim, embed_dim, noise_scale, IND_range, OOD_range, seed)

        assert embed_dim == latent_dim
        assert latent_dim > 30

        # Network topology
        self.g = nx.erdos_renyi_graph(self.latent_dim, p_edge)

        # Model configuration
        self.config = mc.Configuration()
        self.config.add_model_parameter("epsilon", epsilon)
        self.config.add_model_parameter("gamma", gamma)
        self.config.add_model_parameter("k", n_media)
        self.config.add_model_parameter("p", p_interaction)
        self.config.add_model_parameter("gamma_media", gamma_media)

    def create_model(self, x0):
        self.model = op.AlgorithmicBiasMediaModel(self.g)
        self.model.set_initial_status(self.config)
        self.model.status = x0
        self.model.initial_status = x0