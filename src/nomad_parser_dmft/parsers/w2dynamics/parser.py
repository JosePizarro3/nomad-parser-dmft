from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config

from nomad_parser_dmft.parsers.w2dynamics.legacy.parser import LegacyW2DynamicsParser

configuration = config.get_plugin_entry_point(
    'nomad_parser_dmft.parsers:w2dynamics_parser_entry_point'
)


class W2DynamicsParser:
    def parse(
        self,
        filepath: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
    ) -> None:
        LegacyW2DynamicsParser().parse(filepath, archive, logger)
        print('hey W2Dynamics')
