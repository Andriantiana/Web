library(shiny) # il faut charger le package au début de chacun des scripts

shinyServer( function(input, output) { # les éléments de la partie 'server' vont être définis ici
  
  output$sortie_texte <- renderText({ # fonction réactive 'shiny' utilisée pour afficher du texte dans une interface 'UI', ici le résultat de cet élément sera assigné à 'sortie_texte'
    
      paste0("Texte entré : ", input$entree_texte, 
             ". Ce texte comporte ", nchar(input$entree_texte), " caractères.")
      # la ligne ci-dessus permet de concaténer du texte (entre guillemets) et le texte récupéré depuis la partie 'UI' qui est stocké dans 'entree_texte'(NB: nchar() est une fonction R permettant le calcul du nombre de caractères dans une chaîne de caractères)
    
  })

})

