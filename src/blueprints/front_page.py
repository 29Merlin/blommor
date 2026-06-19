from flask import Blueprint, render_template
from forms import SearchForm

def create_blueprint():
    front_page = Blueprint('front_page', __name__)

    @front_page.route('/', methods=['GET', 'POST'])
    def index():
        search_form = SearchForm()
        
        if search_form.validate_on_submit():
            # Handle the search logic here
            search_query = search_form.search.data
            # TODO: Implement search functionality
            print(f"Search query: {search_query}")
        
        return render_template('front_page.html', search_form=search_form)

    return front_page
