from typing import List
from langsmith import Client
from src.helpers.load_env import load_env
from langsmith.schemas import ExampleUploadWithAttachments, Attachment
from src.helpers.load_file import load_file

load_env()

client = Client()


def upload_attachments(dataset_id: str, attachments: List[dict]):
    print("Loading files")

    # Create attachments for all files
    file_attachments = {}
    for index, attachment in enumerate(attachments, 1):
        file_data = load_file(attachment["path"])
        file_attachments[f"file_{index}"] = Attachment(
            data=file_data, mime_type=attachment["mime_type"]
        )

    # Create single example with all attachments
    example = ExampleUploadWithAttachments(
        inputs={"question": "What do you see in these files?"},
        outputs={"answer": "I see an image and a PDF document"},
        attachments=file_attachments,
    )

    print("Uploading example")
    client.upload_examples_multipart(dataset_id=dataset_id, uploads=[example])

    print("Uploaded example")


if __name__ == "__main__":
    dataset = "3657e79f-6755-4481-a748-b77c5f2af575"

    attachments = [
        {
            "path": "/home/juancjc/study/AI/llm-laboratory/files/images/images_images.jpeg",
            "mime_type": "image/jpeg",
        },
        # {
        # 	"path": "/home/juancjc/study/AI/llm-laboratory/files/pdfs/barbershop_example.pdf",
        # 	"mime_type": "application/pdf"
        # }
    ]

    upload_attachments(dataset, attachments)
