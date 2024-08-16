import os
import streamlit as st
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()

notion = Client(auth=os.environ["NOTION_API_KEY"])

page_id = '09f9593420644b33a610079ff12458e0'

def fetch_notion_content():
    response = notion.blocks.children.list(block_id=page_id)
    return response['results']

def display_notion_content():
    st.title("Notion Page Content")
    
    blocks = fetch_notion_content()
    
    for block in blocks:
        if block['type'] == 'callout':
            text_content = ''.join([text['plain_text'] for text in block['callout']['rich_text']])
            st.info(f"Callout: {text_content}")
        elif block['type'] == 'child_database':
            st.subheader(f"Child Database: {block['child_database']['title']}")
        else:
            st.write(f"Unknown block type: {block['type']}")

if __name__ == "__main__":
    display_notion_content()
