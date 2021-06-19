node{
    stage("Clone repository"){
        git  "https://github.com/david22118/WorldOfGames"
    }
    stage("Build and run image"){
        bat "docker build -t games ."
        bat "docker run -d -p 8777:8777 --name games_container --mount source=myvol,target=/app games"
    }
}