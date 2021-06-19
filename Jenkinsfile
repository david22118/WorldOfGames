node{
    stage("Clone repository"){
        git  "https://github.com/david22118/WorldOfGames"
    }
    stage("Build and run image"){
        bat "docker build -t games ."
        bat "docker run -d -p 8777:8777 --name games_container --mount source=myvol,target=/app games"
    }
    stage("Run test"){
        bat "cd tests && python e2e.py"
    }
    stage("Push to DockerHub"){
        bat "docker tag games davidy22118/games"
        bat "docker push davidy22118/games"
    }
     stage("Terminate container"){
        bat "docker rm -vf games_container"
        bat "docker image rm -f games"
    }
}