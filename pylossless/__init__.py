"""Python port of EEG-IP-L pipeline for preprocessing EEG."""

from . import pipeline, config, bids
from .pipeline import LosslessPipeline
from .rejection import RejectionPolicy
from .config import Config
