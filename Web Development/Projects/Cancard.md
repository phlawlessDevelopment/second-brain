## Languages

- [[Javascript]]
- [[NodeJs]]
- [[Typescript]]
- [[Python]]

## Tech stack
- [[Nuxt]] (server side [[Vue]] framework)
- [[Express]]
- [[Pm2]]
- [[Tailwind]]


## Useful Commands
```shell

ssh root@64.227.9.94 # staging   
ssh root@64.227.32.248 # production

pm2 stop staging-microservices # stop server
pm2 restart staging-microservices # start or restart server

```

## github

```
git push origin production
git push origin staging
```


## other shell stuff

##### stop all processes (staging)
``` shell
(
low=4000;
high=4019;
for i in `seq $low $high`; do
  kill -9 $(lsof -t -i:$i);
done
) &&

```

##### stop all processes (production) <span style="color:red"> DANGEROUS</span>
```
``` shell
(
low=3000;
high=3019;
for i in `seq $low $high`; do
  kill -9 $(lsof -t -i:$i);
done
)

```
