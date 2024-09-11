
from pydantic import Field

from nomad.config.models.plugins import ParserEntryPoint


class EntryPoint(ParserEntryPoint):
    parser_class_name: str = Field(
        description="""
        The fully qualified name of the Python class that implements the parser.
        This class must have a function `def parse(self, mainfile, archive, logger)`.
    """
    )
    level: int = Field(
        0,
        description="""
        Order of execution of parser with respect to other parsers.
    """,
    )

    def load(self):
        from nomad.parsing import MatchingParserInterface

        return MatchingParserInterface(**self.dict())


edmft_parser_entry_point = EntryPoint(
    name='parsers/edmft',
    aliases=['parsers/edmft'],
    description='NOMAD parser for eDMFT.',
    mainfile_contents_re=r'\-\-\-\s*Preparing GF calculation\s*\-\-\-',
    mainfile_name_re=r'^.*\.(out)$',
    parser_class_name='nomad_parser_dmft.parsers.edmft.parser.EDMFTParser',
    level=2,
)

soliddmft_parser_entry_point = EntryPoint(
    name='parsers/soliddmft',
    aliases=['parsers/soliddmft'],
    description='NOMAD parser for soliddmft.',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={
        '__has_all_keys': ['dft_input', 'DMFT_input', 'DMFT_results']
    },
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
    parser_class_name='nomad_parser_dmft.parsers.soliddmft.parser.SolidDMFTParser',
)

w2dynamics_parser_entry_point = EntryPoint(
    name='parsers/w2dynamics',
    aliases=['parsers/w2dynamics'],
    description='NOMAD parser for w2dynamics.',
    mainfile_binary_header_re=b'^\\x89HDF',
    mainfile_contents_dict={'__has_all_keys': ['.axes', '.config', '.quantities']},
    mainfile_mime_re='(application/x-hdf)',
    mainfile_name_re=r'^.*\.(h5|hdf5)$',
    parser_class_name='nomad_parser_dmft.parsers.w2dynamics.parser.W2DynamicsParser',
    level=2,
)
