# project_3--api-jordan-stewart-noelle-sif

Name: *Discuss with group*

Purpose: *Discuss with group*











Potential APIs:

    Video Games:

    Books:

    Movies:
        -IMDb = https://imdb-api.com/API
        --#sometimes request go through or not--
        
            -API to search for anything with the expression inside it  = .get('https://imdb-api.com/{lang?}/API/Search?/{apiKey}/{expression}')

                -for extremely specific searches = .get('https://imdb-api.com/{lang?}/API/AdvancedSearch/{apiKey}/?parameters=values')

            -API to make an exact search with all things related to it = .get('https://imdb-api.com/{lang?}/API/Title/{apiKey}/{id}/{options?}')
            
        -MooviesAPI = https://mooviesapi.herokuapp.com/api/

            - .get('https://mooviesapi.herokuapp.com/api/movies/')


        OpenMovieDb = https://www.omdbapi.com/

            get('http://www.omdbapi.com/?apikey={your key}&t={title}&y={year}&plot={short/full}')