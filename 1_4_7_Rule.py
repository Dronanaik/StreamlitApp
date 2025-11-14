import streamlit as st
import json
import os
from datetime import datetime

# File to store topics
TOPICS_FILE = 'topics.json'

# Stages in order
STAGES = ['day1', 'day4', 'day7', 'memory']
NEXT_STAGE = {'day1': 'day4', 'day4': 'day7', 'day7': 'memory'}

def load_topics():
    if os.path.exists(TOPICS_FILE):
        with open(TOPICS_FILE, 'r') as f:
            data = json.load(f)
            # Convert created_at back to datetime if needed, but for simplicity, keep as string
            return data
    return []

def save_topics(topics):
    with open(TOPICS_FILE, 'w') as f:
        json.dump(topics, f, indent=4)

def main():
    st.title("1-4-7 Rule Study App")

    # Load topics
    if 'topics' not in st.session_state:
        st.session_state.topics = load_topics()

    # Add new topic
    st.header("Add New Topic")
    new_topic = st.text_input("Enter topic name:")
    if st.button("Add Topic"):
        if new_topic.strip():
            topic = {
                'name': new_topic.strip(),
                'stage': 'day1',
                'created_at': datetime.now().isoformat(),
                'last_reviewed': datetime.now().isoformat()
            }
            st.session_state.topics.append(topic)
            save_topics(st.session_state.topics)
            st.success(f"Added topic: {new_topic}")
            st.rerun()  # Refresh to clear input

    # Display topics by stage
    for stage in STAGES:
        st.header(f"Stage: {stage.replace('day', 'Day ')}")
        stage_topics = [t for t in st.session_state.topics if t['stage'] == stage]
        if not stage_topics:
            st.write("No topics in this stage.")
        else:
            for i, topic in enumerate(stage_topics):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{topic['name']}** (Created: {topic['created_at'][:10]})")
                with col2:
                    if stage != 'memory':
                        if st.button(f"Mark Reviewed", key=f"{stage}_{i}"):
                            topic['stage'] = NEXT_STAGE[stage]
                            topic['last_reviewed'] = datetime.now().isoformat()
                            save_topics(st.session_state.topics)
                            st.rerun()

if __name__ == "__main__":
    main()