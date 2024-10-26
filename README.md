# Nicolas Cage App 🎬
This is a data-driven interface that presents fun and insightful facts about Nicolas Cage's filmography. This app is written in Python, and is hosted with Streamlit. It showcases Nicolas Cage's unique contributions to cinema through data visualizations. 

## App Features

Here are some of the features the app provides:
- **Top Movies**: View the highest-rated Nicolas Cage films with key details.
- **Rating Distribution**: Visualize how Cage's movies perform across rating categories.
- **Genre Diversity**: Explore the genres in which Cage made his mark.
- **Career Timeline**: See the number of movies Cage has acted in over time.

## Dataset

The dataset, `imdb-movies-dataset.csv`, contains detailed information about various movies, including cast, genre, ratings, and more. <br />
**[Download the dataset here](https://github.com/Sasha-Solo/Nicolas-Cage-App/blob/main/imdb.csv.zip)**

## Try It Out

The app is hosted on Streamlit Cloud. You can view the application at this URL:<br>
**[Nicolas Cage Filmography App](https://nicolas-cage-app-fmfqdycgm4grtfmz533aba.streamlit.app/)**  

Alternatively, you can run the app locally:

---

### Running Locally

1. **Clone the Repository**  
    ```bash
    git clone https://github.com/Sasha-Solo/Nicolas-Cage-App.git
    cd Nicolas-Cage-App
    ```

2. **Set Up a Virtual Environment**<br>
    ```bash
    python -m venv .venv
    ```
    <strong>Activate</strong>:
    - Windows: `.venv\Scripts\activate`  
    - MacOS/Linux: `source .venv/bin/activate`

3. **Install Required Libraries**<br>
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App**<br>
    ```bash
    streamlit run app.py
    ```
