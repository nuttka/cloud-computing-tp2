while getopts f:t: opts; do
   case ${opts} in
      t) text=${OPTARG} ;;
   esac
done


cluster_ip=$(kubectl get svc ml-twitter-service -ojsonpath='{.spec.clusterIP}')

wget --server-response --output-document response.json --header='Content-Type: application/json' --post-data "{\"text\": \"$text\"}" http://${cluster_ip}:5019/api/american &> /dev/null

python -m json.tool response.json
