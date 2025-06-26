# ✨Let’s Start the Project ✨
## **Part 1: Clone du repo Github **
### **Step 1: Clone du code**
Clone le code à partir du repository :

```
git clone https://github.com/AhmedKhnissi/File-downloader.git
```
### **Step 2: Installation des dépendences**

L'application utilise à la base les librairies **`Flask` et **`pytest` on les installe à partir de pip:
 
```
pip install -r requirements.txt
```

### **Step 3: Démarage de l'application**
Avant de commencer cette partie :
```jsx
✅ test_index
But : Vérifie que la page d’accueil (/) est accessible.

Ce que le test valide :

Le code HTTP est 200 OK.

Le texte "Fichiers disponibles" est bien présent dans la page HTML retournée.
```

```jsx
✅ test_api_files
But : Vérifie que l’API REST (/api/files) retourne la liste des fichiers.

Ce que le test valide :

Le code HTTP est 200 OK.

La réponse est bien une liste JSON ([]) contenant les noms des fichiers dans le volume.
```

```jsx
✅ test_download_file
But : Teste le bon fonctionnement de la route de téléchargement /download/<filename>.

Ce que le test fait :

Crée un fichier temporaire example.txt dans le dossier monté.

Envoie une requête pour le télécharger.

Vérifie que le code de réponse est 200 OK.

Vérifie que le contenu retourné contient bien "Test file content".

Supprime ensuite le fichier (nettoyage).
```

Pour lancer manuellement les tests unitaires : 
```
python -m pytest test_app.py
```

pour démarer l'application vous devez utiliser cette commande : 

```
python.exe .\app.py
```
Ceci va lancer le serveur Flask sur cette url : 

```
192.168.1.169:5000/
```

### **Step 4: Conteneurisation de l'application**
Voila le contenu du Dockerfile :
Ici, j’ai défini /app comme répertoire de travail. Après, j’ai installé les modules dans requirements.txt sur le répertoire de Docker, et à la fin, je lance le script qui se trouve dans le fichier entrypoint.sh pour soit lancer les tests unitaires, soit lancer l'application.

```jsx
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]

```

Comme vous pouvez le voir sur l'image ci-dessus, on a notre application conteneurisée, taguée et poussée vers mon Docker Hub personnel, afin d’appeler ensuite l'image Docker directement depuis n'importe où et lancer l'application.

![Image](https://github.com/user-attachments/assets/3de195e9-1bdc-4865-96e5-6611c14298e3)


### **Step 5: lancement de l'application à travers docker**

Ici, on récupère l'image de Docker Hub afin d'exécuter les tests unitaires avant de lancer l'application,
à travers le  **`RUN_MODE=test` qu'on defini dans un fichier **`shell` d'automatisation appeler entrypoint.sh lancer à partir de l'image docker elle meme 
```jsx
docker pull flask-app
docker run --rm -e RUN_MODE=test -v "${PWD}:/app" flask-app
```

Finalement en lance le contenur docker par cette commande 

```
docker run -d -p 5000:5000 -v "${PWD}:/app" flask-app

```

on peut trouveer les resultats des tests dans le fichier **`resultats_tests.txt` 


### **Step 6: Les interfaces de l'application**

Pour commencer, vous pouvez tester l’endpoint de téléchargement soit par le bouton de téléchargement lui-même, qui se trouve sur chaque fichier dans la page d’accueil, soit en tapant cette URL :
```
192.168.1.169:5000/download/test.txt
```

soit i l ya l'end point de l'api
```
192.168.1.169:5000/api/files
```
![Image](https://github.com/user-attachments/assets/421543c1-b56a-4587-a6d4-3d76952e3ed9)

# **  Résultat Finale ! **  
![Image](https://github.com/user-attachments/assets/f5b13e4c-9860-4f0f-8a90-254a8ac2b85a)
