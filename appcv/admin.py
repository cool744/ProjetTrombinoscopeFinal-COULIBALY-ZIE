from django.contrib import admin
from .models import Personne, Experience, Formation, Competence, Langue, Contact, CV, Loisir

from .models import Inclure, Formation, Associer, Langue, Rajouter, Competence, Posseder
@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    # Champs affichés dans la liste des CVs
    list_display = ['title', 'personne', 'user', 'design']
    # Champs pour filtrer
    list_filter = ['design']
    # Champs éditables directement depuis la liste
    list_editable = ['design']
    # Champs de recherche
    search_fields = ['title', 'personne__nom', 'personne__prenom']

# Enregistrement des autres modèles sans personnalisation
admin.site.register(Personne)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(Competence)
admin.site.register(Langue)
admin.site.register(Contact)
admin.site.register(Loisir)

# Admin for Inclure model
class InclureAdmin(admin.ModelAdmin):
    list_display = ('cv', 'experience')
    search_fields = ('cv__user__username',)

admin.site.register(Inclure, InclureAdmin)


class AssocierAdmin(admin.ModelAdmin):
    list_display = ('cv', 'formation')
    search_fields = ('cv__user__username',)

admin.site.register(Associer, AssocierAdmin)


class RajouterAdmin(admin.ModelAdmin):
    list_display = ('cv', 'langue')
    search_fields = ('cv__user__username',)

admin.site.register(Rajouter, RajouterAdmin)

class PossederAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'competence')
    search_fields = ('etudiant__username', 'competence__libelle')

admin.site.register(Posseder, PossederAdmin)


