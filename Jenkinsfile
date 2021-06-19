node{
    stage("Clone repository"){
        git  "https://github.com/david22118/WorldOfGames"
    }
    stage("Build and run image"){
        bat "docker build -t games ."
        bat "docker run -d -p 8777:8777 --name games_container --mount source=myvol,target=/app games"
    }
    stage("Run test"){
        bat  "cd test"
        bat  "python e2e.py"
    }
    stage("Push to DockerHub"){
        bat  "bat 'docker push davidy22118/games'"
    }
     stage("Terminate container"){
        bat  "docker rm -vf $(docker ps -a -q)"
        bat  "docker rmi -f $(docker images -a -q)"
    }
}