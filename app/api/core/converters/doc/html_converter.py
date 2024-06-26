from api.core.converters.base_converter import BaseConverter
import logging

logger = logging.getLogger(__name__)


class HtmlConverter(BaseConverter):

    @classmethod
    def allowed_formats(cls) -> list[str]:
        return ["htm", "html"]

    def convert_htm(self, **kwargs) -> str:
        # use unstructured
        return self.convert_html(**kwargs)

    def convert_html(self, **kwargs) -> str:
        # use unstructured
        from unstructured.partition.html import partition_html

        logger.info(f"Converting [{self.file}] with unstructured converter")

        pptx_elements = partition_html(self.file)
        raw = "\n".join([element.text for element in pptx_elements])

        return raw

    def process(self, **kwargs) -> str:
        if self.file_info.file_type == "htm":
            raw = self.convert_htm(**kwargs)
        elif self.file_info.file_type == "html":
            raw = self.convert_html(**kwargs)
        else:
            raise ValueError(f"Unsupported file type: {self.file_info.file_type}")

        return raw
