# Animal Store

Simple django app for adding animals to a PostgreSQL db that looks presentable with the help of some bootstrap.
Animals joined with tags that people can also add, delete and search with.

Animal data:

* name
* category (mammal/fish/amphibian/reptile/bird)
* imageURL
* status (placed/approved/delivered)
* tags

# API:

* curl --header "Content-Type:application/json" --request POST --data '{"id" : "", "animalName": "", "category": "", "imageURl": "", "status": ""}' http://_localhost_/api/entry/

* curl --header "Content-Type:application/json" --request POST --data '{"id" : "", "animalName": "", "category": "", "imageURl": "", "status": ""}' http://_localhost_/api/delete/ ( giving only "id" is enough)

* curl --header "Content-Type:application/json" --request POST --data '{"id" : "", "animalName": "", "category": "", "imageURl": "", "status": ""}' http://_localhost_/api/edit/

* http://_localhost_/animal-store/animal-list/ - json data response