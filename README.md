<h3>Bank Note Authentication:</h3>
Data was extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

1. [Flasgger](https://www.github.com/flasgger/flasgger)

```
pip install flasgger
```

2. [SpyderIDE](https://www.spyder-ide.org/)

3. [Flask](https://flask.palletsprojects.com/en/2.3.x/)

4. [Github](https://www.github.com/)

5. [Python](https://www.python.org/)

6. [JupyterNotebook](https://jupyter.org/)

<h3>How to predict using a file?</h3>
We use postman, steps to be followed:
1. Set the hyperlink
2. Select the method as "POST"
3. Go to "Body" => "form-data" => Change "text" to "file"

To create a environment:

```
    conda create -p venv_bank python==3.7 -y
```

To activate environment:

```
    conda activate venv_bank/
```

To run flassger:

```
    python app_flassger.py
    On browser: http://127.0.0.1:5000/apidocs/
```

To run streamlit:

```
    streamlit run app_streamlit.py
```

To build a docker image:

```
    docker built -t name_of_api .
```

To see docker built:

```
    docker ps
```

To run docker:

```
    docker run -p 8080:8080 name_of_api
```

For browsing, browse using:

```
    IP_of_docker:port_no/apidocs
```
