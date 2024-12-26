import os
from datetime import datetime
import json

def save_conversation(conversation, metadata=None):
    messages = [msg.dict() for msg in conversation]

    # Create history directory if it doesn't exist
    if not os.path.exists('history'):
        os.makedirs('history')

    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"history/chat_{timestamp}.txt"

    # Add additional info to existing metadata
    if metadata:
        metadata.update({
            "filename": filename,
        })

    # Save conversation to file with metadata header
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=== Metadata ===\n")
        f.write(json.dumps(metadata, indent=2, default=str))
        f.write("\n\n=== Conversation ===\n")
        f.write('\n'.join(str(msg) for msg in messages))