import os
import errno

#indice =4


for indice in range(1, 100):
    print(indice)
    filename = f"C:\\Pervasivemind.net\\Lab\\argocd-example\\helm-values-files\\kuard{indice}\\kuard.yaml"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        f.write(f'''yotpo:
    deploymentName: kuard-test{indice}
    chartName: onechart
    chartPath: https://chart.onechart.dev/
    chartVersion: v0.41.0
    namespace: kuard-test{indice}

    replicaCount: 1
    image:
    repository: gcr.io/kuar-demo/kuard-amd64
    tag: blue

    containerPort: 8080
    imagePullSecrets: []

    ## Configure args passed to Telegraf containers
    args: []
        ''')
