library(shiny)
shinyUI(pageWithSidebar(
    headerPanel("Premier exemple"),
	sidebarPanel(
	    textInput(inputId = "entree_texte",
		          label = "Entrez du texte:",
				  value = "")
				),
	mainPanel(
	    h3("Voici le texte que vous avez entré:"),
		textOutput("sortie_texte")
		)
	))