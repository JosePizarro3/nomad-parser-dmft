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

from nomad_parser_dmft.parsers.soliddmft.legacy.parser import LegacySolidDMFTParser


configuration = config.get_plugin_entry_point(
    'nomad_parser_dmft:soliddmft_parser_entry_point'
)


class SolidDMFTParser:
    def parse(
        self,
        filepath: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
    ) -> None:
        LegacySolidDMFTParser().parse(filepath, archive, logger)
        print('hey SolidDMFT')