from numpy import product
from app import app
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index(name="Hello World"):
    return render_template("index.html.jinja", text=name)

@app.route('/extract/<product_id>')
def extract(product_id):
        url = f"https://www.ceneo.pl/{product_id}#tab=reviews"
    all_opinions = []
    while(url):
        response=requests.get(url)

        page = BeautifulSoup(response.text, 'html.parser')

        opinions = page.select("div.js_product-review")
        for opinion in opinions:       
            single_opinion = {
                key:get_item(opinion, *value)
                for key, value in selectors.items()
            }
            single_opinion["opinion_id"] = opinion["data-entry-id"]
            all_opinions.append(single_opinion)
        try:
            url = "https://www.ceneo.pl" + get_item(page, 'a.pagination__next', 'href')
        except TypeError:
            url = None

    with open(f"opinions/{product_id}.json", 'w', encoding='UTF_8') as jf:
        json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
        return redirect(url_for("product", product_id=product_id))

@app.route('/products')
def products():
    products

@app.route('/author')
def author():
    pass

@app.route('/product/<product_id>')
def product():
    pass

