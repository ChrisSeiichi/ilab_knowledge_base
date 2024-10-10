import os

def split_markdown(input_file, max_words=500):
    # Read the content of the markdown file
    file_dir = "yaml_construction/context/raw"
    with open(os.path.join(file_dir, input_file), 'r') as f:
        content = f.read()
    
    # Split the content into chunks of max_words
    words = content.split()
    chunks = [words[i:i + max_words] for i in range(0, len(words), max_words)]
    
    # Create separate folder
    output_dir="yaml_construction/context/reduced"
    output_folder=os.path.join(output_dir, input_file)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Write each chunk to a separate markdown file
    for i, chunk in enumerate(chunks):
        chunk_content = ' '.join(chunk)
        output_file = os.path.join(output_folder, f"part_{i+1}.md")
        with open(output_file, 'w') as f:
            f.write(chunk_content)
        
        print(f"Created: {output_file}")

split_markdown(input_file="models-managing-data-model-evaluations.md", max_words=500)
