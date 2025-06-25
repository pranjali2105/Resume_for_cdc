from langchain_groq import ChatGroq
from datetime import datetime

class ConsolidationLlama:
    def __init__(self, name="llama-3.1-70b-versatile"):
        self.name = name
        self.model_name = name

    def process(self, to_input):
        current_date = datetime.now().strftime("%-d %B %Y")
        prompt = (
            "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
            "Environment: ipython\n"
            "Tools: brave_search, wolfram_alpha\n"
            "Cutting Knowledge Date: December 2023\n"
            f"Today Date: {current_date}\n"
            "You are an advanced image summary consolidation assistant. Your task is to convert information about each part of the image into a concise, clear, and comprehensive summary.<|eot_id|>\n"
            "<|start_header_id|>user<|end_header_id|>\n"
            f"Based on the following analysis of an image: {to_input}, consolidate all the information, highlighting the key insights, relationships, and any potential inferences. Please ensure the summary is concise yet comprehensive.<|eot_id|>\n"
            "<|start_header_id|>assistant<|end_header_id|>\n"
        )
        response = ChatGroq(temperature=0, groq_api_key="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", model_name=self.model_name).invoke(prompt)
        return response.content

# some_data = [
#     "the dog is brown",
#     "the dog is small and cute"
#     "the flower garden has orange flowers and green grass"
# ]
# consolidator = ConsolidationLlama()
# print(consolidator.process(some_data))

#output:
# Based on the analysis of the image, the key insights are:

# * The dog is brown, small, and cute.
# * The flower garden has orange flowers and green grass.

# The relationships between these elements are:

# * The dog is likely in the flower garden, as both are mentioned in the same context.
# * The orange flowers and green grass create a visually appealing and vibrant atmosphere, which complements the cuteness of the dog.

# Potential inferences:

# * The image is likely a serene and peaceful scene, with the dog enjoying the beautiful surroundings.
# * The image may be taken in a natural setting, such as a park or a backyard, given the presence of a flower garden.

# Overall, the image appears to be a heartwarming and idyllic scene, showcasing the beauty of nature and the joy of a small dog in a vibrant flower garden.
