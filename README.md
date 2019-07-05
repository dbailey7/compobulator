# compobulator

This Django project (compobulator_project) has an app (compobulator_app), a couple models (Mp_archetype, 
Mp_Element), a TemplateView (IndexView), a couple ListViews (ArchetypeListView, ElementListView), a couple 
DetailViews (ArchetypeDetailView, ElementDetailView) and a couple forms (mp_archetype_form_view, 
mp_element_form_view).  

The forms create some data.  The ListVews list the data created via the forms.  

And the DetailViews are "supposed" to display the detail records when the links in the ListViews are clicked on, 
but that's not happening.

When the ListView links are clicked on, nothing is displayed.  No error messages are displayed, either.

The project's folder structure is as follows:

• compobulator_container folder

• • compobulator_project folder

    manage.py
    
• • • compobulator_app folder

      __init__.py
      admin.py
      apps.py
      forms.py
      models.py
      tests.py
      urls.py
      views.py
      
• • • • migrations folder

        __init__.py
        0001_initial.py
        0002_mp_element_archetypeid.py
        0003_auto_20190627_0808.py
        
• • • • templates folder

• • • • • compobulator_app folder

          compobulator_app_base.html
          mp_archetype_detail.html
          mp_archetype_form.html
          mp_archetype_list.html
          mp_element_detail.html
          mp_element_form.html
          mp_element_list.html
          
• • • compobulator_project folder

      __init__.py
      settings.py
      urls.py
      wsgi.py
      
• • • media folder

• • • static folder

• • • templates folder

• • • • compobulator_app

        base.html
        undex.html
        
• • static folder

• • • admin folder

• • • css

      meedstyles.css
      
• • • customthemes

• • • • css

        meedmaster.css
        
• • • images

      favicon.ico
      meedlogo.png
