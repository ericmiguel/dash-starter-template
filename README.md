# Dash Starter Template
A [Dash](https://dash.plotly.com) starter template, suitable for small to large projects with AWS serverless deployment in mind.


# dependencies
- Flask
- Dash
- Zappa

## project setup

```
pip install -r requirements.txt
npm install
```

## CSS customization

See [Bulma docs](https://bulma.io/documentation/customize/) for more specific instructions.

```
# after edit style.scss at sass folder
npm run css-build
```

## run

```
export FLASK_ENV=development
flask run
# or 
python run.py
```

## deployment

*under development*