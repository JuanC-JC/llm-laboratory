prompt = """
json example:
{
'document_overview': 'Provide a brief general description of the document content and its main purpose',
'business_name': 'Extract the name of the business',
'business_description': 'Extract the description of the business',
'products_and_services': [
    {
    'title': 'Extract the name/title of the product or service',
    'description': 'Extract the detailed description',
    'price': 'Extract the price if available (use null if not found), the price should be a numeric value',
    'type': 'Determine if it is a product or service (use values: product or service)'
    }
],
'FAQ': [
    {
    'question': 'Extract the question',
    'answer': 'Extract the answer'
    }
],
'schedule': [
    {
    'day': 'Extract the day of the week', // 0 sunday, 1 monday, 2 tuesday, 3 wednesday, 4 thursday, 5 friday, 6 saturday
    'start_time': 'Extract the start time', // 1900 is 19:00
    'end_time': 'Extract the end time' // 0800 is 08:00
    }
],
'domain': 'Extract the domain of the website'
}


Please analyze the provided document and extract information about products and services mentioned within it.  Adhere strictly to the JSON structure above when formatting your output.

**Instructions:**

1. **Document Overview:** Begin by providing a concise and informative overview of the document's content and main purpose in the `document_overview` field. include the language of the document.

2. **Business Name and Description:** Extract the name of the business and its description in the `business_name` and `business_description` fields. if no business name and description is found, create some according to the information in the document.

3. **Products and Services Extraction:** Extract all instances of products and services mentioned in the document. For each product or service, create a JSON object within the `products_and_services` array, populating the following fields:
    * `title`: Extract the exact name or title of the product or service.
    * `description`: Extract a detailed description of the product or service, capturing its key features and functionalities. if no description is found, generate a description based on the title.
    * `price`: If a price is explicitly mentioned, extract it as a numeric value. If no price is found, use `null` for this field.
    * `type`: Categorize the item as either a "product" or "service." Ensure the value for this field is strictly either `"product"` or `"service"`.

3. **Completeness and Accuracy:** Ensure that each item in the `products_and_services` array includes all four fields (`title`, `description`, `price`, and `type`). Prioritize accuracy in extracting information and avoid any hallucinations or assumptions.

4. **Thorough Extraction:** Extract as many products and services as you can identify within the document while maintaining accuracy and adherence to the specified JSON structure.

5. **FAQ Extraction:** Extract all instances of questions and answers from the document. For each question-answer pair, create a JSON object within the `FAQ` array, populating the following fields:
    * `question`: Extract the question.
    * `answer`: Extract the answer.
    if no question and answer is found, create some according to the information in the document.

6. **Schedule Extraction:** Extract all instances of the schedule from the document. For each schedule item, create a JSON object within the `schedule` array, populating the following fields:
    * `day`: Extract the day of the week.
    * `start_time`: Extract the start time.
    * `end_time`: Extract the end time.
    only one schedule item per day and If the start and end time is not clear, take the earliest and latest time

7. **Domain Extraction:** Extract the domain of the website from the document.

8. **Original Language:** All extracted information should be in the original language of the PDF document. Do not translate any extracted text.

IMPORTANT: All information must be in the language of the document
"""
