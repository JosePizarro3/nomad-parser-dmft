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

from nomad_parser_dmft.parsers.edmft.legacy.parser import LegacyEDMFTParser


configuration = config.get_plugin_entry_point(
    'nomad_parser_dmft:edmft_parser_entry_point'
)


class EDMFTParser:
    def parse(
        self,
        filepath: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
    ) -> None:

        print('hey EDMFT')
        LegacyEDMFTParser().parse(filepath, archive, logger)
