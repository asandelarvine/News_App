from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting sources by category
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title, general = general_sources, business = business_sources, technology = technology_sources, sports = sports_sources,)

@main.route('/articles/<source>')
def articles(source):
    '''
    View articles for a specific source page function that returns the article details page and its data
    '''
    articles = get_articles(source)

    return render_template('article.html', articles = articles)