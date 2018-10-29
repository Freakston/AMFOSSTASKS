var xmlhttpp = new XMLHttpRequest();



function search(){
        var name = document.getElementById("pk_name").value;
        xmlhttpp.open("GET","https://pokeapi.co/api/v2/pokemon/" , true);
        xmlhttpp.send();
        xmlhttpp.onload = function(){
                var myObj = JSON.parse(this.responseText);
                console.log(name);
                console.log(myObj);     
        }
};


function search_Pokemon(){
        var search = document.getElementById("Pokemon_name").value;

        search_req.open('GET', "https://pokeapi.co/api/v2/pokemon/"+search.toLowerCase()+'/',true)

        search_req.onload = function (){
                                var data=JSON.parse(this.responseText);
                                console.log(data);


                                var Name=data.name.toUpperCase();
                                document.getElementById("name").innerHTML =Name;
                                document.getElementById("img").innerHTML = '<img style="width: 200px;" src="' + data.sprites.front_default + '">';

                                var x=data.abilities.length;
                                var abilityList = "";
                                var i;

                                for (i = 0; i < x; i++) {
                                abilityList += '<li>' + data.abilities[i].ability.name + '</li>';
                                }

                                document.getElementById("ability").innerHTML = "Abilities are: <br>" + abilityList;

                                var y=data.types.length;
                                var typeList= "";
                                var j;

                                for (j = 0; j <=y; j++) {
                                typeList+= '<li>' + data.types[j].type.name + '</li>';
                                }

                                document.getElementById("type").innerHTML = "Pokemon types are: <br>" + typeList;

                                }
        search_req.send();
        }

