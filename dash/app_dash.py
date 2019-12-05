import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# On définit une feuille de style
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# On ajoute la feuille de style à l'application
app = dash.Dash(external_stylesheets = external_stylesheets)

app.layout = html.Div(
    children=[
        # Les dropdowns permettent d'afficher un menu déroulant
        # 'options' permet de créer les choix du menu déroulant
        # 'id' représente le nom caché du dropdown (pour les callbacks)
        # 'clearable'(=True) pour permettre de vider le dropdown
        # 'multi'(=False) pour activer la multi-selection
        # 'placeholder' pour mettre un texte par défaut dans le dropdown si aucune valeur n'est selectionnée
        # 'searchable'(=True) permet d'autoriser la recherche par caractère
        # 'value' permet de définir une valeur par défaut
        dcc.Dropdown(
            options=[
                # 'disabled'(=False) pour désactiver une option en la laissant visible
                {'label': 'Mon premier choix', 'value': 'ID de ce choix'},
                {'label': "C'est ce champ qui compte, et il est désactivé", 'value': '2', 'disabled': 'True'},
                {'label': 'Troisième choix', 'value': '3'}
                    ],
            id='A',
            clearable=False,
            multi=True,
            placeholder='Texte par défaut du placeholder',
            searchable=False,
            value='ID de ce choix',
            # Un exemple de style, ici on déplace le graphique de 0 pixels donc cela n'a aucune effet
            style={'marginTop': 0}
                    ),
        
        html.Div(children='Hello'),
        
        # Les sliders permettent d'afficher des jauges
        # 'id' représente le nom caché du composant (pour les callbacks)
        # 'disabled' permet de désactiver la jauge
        # 'dots'(=True) permet d'afficher des points (jauge discrète), ne fonctionne que si step > 1
        # 'max' le maximum de la jauge
        # 'min' le minimum de la jauge
        # 'step'(=1) valeur de déplacement sur la jauge
        # 'updatemode'(=mouseup (ou drag)) permet de choisir entre mettre a jour quand on lâche le curseur ou en continue
        # 'value' valeur par défaut
        # 'vertical'(=False) permet de créer une jauge vertical
        # 'included'(=True) permet de de choisir entre un curseur remplissant une jauge ou un curseur se déplacant seulement
        # 'marks' permet de décrire ce qui est marqué sous la jauge
        dcc.Slider(
            id='B',
            disabled=False,
            dots=True,
            min=0,
            max=10,
            step=20,
            value=50,
            updatemode='drag',
            included=False,
            marks={i: '{}'.format(1 * i) for i in range(11)},
                   ),
        
        # Les Input sont des boites dans lesquelles on peut taper du texte
        # 'id' représente le nom caché du composant (pour les callbacks)
        # 'disabled' permet de désactiver le composant
        # 'value' valeur par défaut
        # 'placeholder' pour mettre un texte par défaut dans le composant si aucune valeur n'est entrée
        dcc.Input(
            id='input',
            type='text',
            value='texte par défaut',
            style={'marginTop': 200},
            placeholder='placeholder'),
        
        # Les buttons sont des boutons
        # 'id' représente le nom caché du composant (pour les callbacks)
        # On peut afficher quelque chose sur le bouton, ici "Nom du bouton"
        # n_clicks(=None) représente le nombre de fois que le composant a été cliqué, on peut lui donner une valeur par défaut
        html.Button(
            'Nom du bouton',
            id='button',
            n_clicks='0'
            ),
        
        # Les graphs sont des graphiques basés sur Plotly
        # 'figure' permet de décrire à quoi ressemblera le graphique
        # 'id' représente le nom caché du composant (pour les callbacks)
        # 'style' permet de styliser le graphique
        dcc.Graph(
            # 'data' permet de remplir le graphique
            figure=go.Figure(
                data=[
                    go.Bar(
                        x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                        2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                        y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                        350, 430, 474, 526, 488, 537, 500, 439],
                        name='Premier histogramme',
                        marker=go.bar.Marker(
                            color='rgb(55, 83, 109)'
                                            )
                           ),
                    go.Bar(
                        x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                        2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                        y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                        299, 340, 403, 549, 499],
                        name='Second histogramme',
                        marker=go.bar.Marker(
                            color='rgb(26, 118, 255)')
                           )
                    ],
                layout=go.Layout(
                    # On donne un nom au graphique, on affiche sa légende et on la définit
                    title='Un super graphique',
                    showlegend=True,
                    legend=go.layout.Legend(
                        x=0,
                        y=1.0),
        )
    ),
            # On définit la taille du graphique
            style={'height': 500},
            id='graph'
    )])

app.run_server(debug=False)