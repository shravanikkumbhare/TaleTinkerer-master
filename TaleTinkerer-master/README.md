# TaleTinkerer 💭

This project implements an interactive storytelling application powered by the OpenAI GPT-3.5 Turbo & DALL-E models. Users can engage with the application by making choices in a story, and the AI generates responses based on the given prompts.

<!--
|  |  |
|---------|---------|
| ![Image_1](app/src/image_1.png) | ![Image_2](app/src/image_2.png) |
| ![Alt text](app/src/image_3.png) | ![Alt text](app/src/image_4.png) |
 -->

<details>
<summary> 🪜 Setup Steps: </summary>

👉 **Create `key.txt` file:**
   - Create a new text file named `key.txt` in the main project structure.
   - Save your OpenAI GPT-3.5 Turbo API key in this file.
   - Ensure that the key is the only content in the file and does not include any extra spaces or characters.

👉 **Install Dependencies:**
   - Open a terminal or command prompt and navigate to the project directory.
   - Run the following command to install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - This will install Flask and OpenAI Python packages.

👉 **Run the Flask Application:**
   - Run the Flask application using the following command:
     ```bash
     python run.py
     ```
   - The application will be accessible at `http://localhost:5001` in your web browser.

👉 **Access the Application:**
   - Open your web browser and go to `http://localhost:5001`.
   - You should now see the Tales of GPT interactive storytelling application.

👉 **Engage with the Story:**
   - Follow the on-screen instructions to engage with the interactive story.
   - Make choices and enjoy the dynamically generated responses by the OpenAI GPT-3.5 Turbo model.

🚀 **Setup using Docker:**
  - Build the Docker image: 
    ``` bash
    docker build -t taletinkerer:latest .
    ```

  - Run the Docker container: 
    ``` bash
    docker run -d -p 5001:5001 taletinkerer
    ```



</details>

<details>
<summary>🚀 Walkthrough TaleTinkerer : </summary>


| Option 1 | Option 3 |
| :--: | :--: |
| ![Image](https://github.com/rudrakshkarpe/TaleTinkerer/assets/78851635/09bdeaaf-dd28-4b9d-94cb-d3991a11d03d) | ![Image](https://github.com/rudrakshkarpe/TaleTinkerer/assets/78851635/16418a74-050c-4ffd-9476-7c1ef81360f2) |
| Option 1 | Option 2 |
| ![Image](https://github.com/rudrakshkarpe/TaleTinkerer/assets/78851635/a2da2221-73c3-41c5-abaa-31b174131577) | ![Image](https://github.com/rudrakshkarpe/TaleTinkerer/assets/78851635/2f78bc09-fef1-4b7a-bb47-fc198819ea23) |

</details>


<details>
<summary>✅ Todo List:</summary>
 
 - [ ] [Wishper](https://openai.com/research/whisper) Integration 
 - [ ] Fix response waiting time
 - [ ] Explore huggingface, midjouney integrations 
</details>
