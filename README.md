# Nicolas Cage App 🎬
A data-driven interface that presents fun and insightful facts about Nicolas Cage's filmography. This app was built with Streamlit, and showcases Nicolas Cage's unique contributions to cinema through data visualizations. 

## App Features

- **Top Movies**: View the highest-rated Nicolas Cage films with key details.
- **Rating Distribution**: Visualize how Cage's movies perform across rating categories.
- **Genre Diversity**: Explore the genres in which Cage made his mark.
- **Career Timeline**: See the number of movie releases over time.

## Dataset

The dataset, `imdb-movies-dataset.csv`, contains detailed information about various movies, including cast, genre, ratings, and more. <br />
**[Download the dataset here](https://github.com/Sasha-Solo/Nicolas-Cage-App/blob/main/imdb.csv.zip)**

## Try It Out

The app is hosted on Streamlit Cloud. Check it out at this URL:<br>
**[Nicolas Cage Filmography App](https://nicolas-cage-app-fmfqdycgm4grtfmz533aba.streamlit.app/)**  
*Note: You’ll need to upload a local copy of the dataset for the app to run.*

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
