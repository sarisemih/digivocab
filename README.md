# DigiVocab

DigiVocab is an application where users can create profiles, manage vocabularies, add words with their meanings and example sentences, and participate in vocabulary exercises. The app includes profile management, a follow/unfollow system, and JWT-based authentication.

## Features

- **Profile Management**: Users can create and manage their profiles.
- **Vocabulary Management**: Add words with meanings and example sentences to vocabularies.
- **Follow/Unfollow System**: Follow or unfollow other users, and view the list of users you follow.
- **JWT Authentication**: Secure authentication with JWT tokens.
- **Exercises**: Participate in vocabulary exercises to test your language knowledge.

## API Endpoints

### **Authorize**
JWT-based authentication for secure access.

- **POST** `/api/profiles/token/`: Obtain JWT access and refresh tokens.
- **POST** `/api/profiles/token/refresh/`: Refresh access token using the refresh token.

### **Exercises**
Manage and participate in vocabulary exercises.

- **GET** `/api/exercises/question/`: Retrieve exercise questions to test vocabulary knowledge.

### **Profiles**
Manage user profiles, follow and unfollow users, and perform profile searches.

- **POST** `/api/profiles/follow/{username}/`: Follow a user by username.
- **GET** `/api/profiles/followed-list/`: Retrieve the list of followed users.
- **POST** `/api/profiles/register/`: Register a new user.
- **GET** `/api/profiles/search/`: Search for profiles by username.
- **POST** `/api/profiles/unfollow/{username}/`: Unfollow a user by username.

### **Vocabularies**
Create and manage vocabularies and words.

- **GET** `/api/vocabularies/`: Retrieve the list of vocabularies.
- **POST** `/api/vocabularies/`: Create a new vocabulary.
- **GET** `/api/vocabularies/{id}/`: Retrieve a specific vocabulary by ID.
- **PUT** `/api/vocabularies/{id}/`: Update a vocabulary by ID.
- **PATCH** `/api/vocabularies/{id}/`: Partially update a vocabulary by ID.
- **DELETE** `/api/vocabularies/{id}/`: Delete a vocabulary by ID.

#### **Words within Vocabularies**
Manage words associated with vocabularies.

- **GET** `/api/vocabularies/{vocabulary_id}/words/`: Retrieve all words in a specific vocabulary.
- **POST** `/api/vocabularies/{vocabulary_id}/words/`: Add a new word to a specific vocabulary.
- **GET** `/api/vocabularies/{vocabulary_id}/words/{word_id}/`: Retrieve details of a specific word.
- **PUT** `/api/vocabularies/{vocabulary_id}/words/{word_id}/`: Update a specific word.
- **PATCH** `/api/vocabularies/{vocabulary_id}/words/{word_id}/`: Partially update a specific word.
- **DELETE** `/api/vocabularies/{vocabulary_id}/words/{word_id}/`: Delete a specific word.

#### **Copy Vocabulary**
- **POST** `/api/vocabularies/{vocabulary_id}/copy/`: Copy an existing vocabulary to a new one.

## Running the Application
Visit [DigiVocab](http://127.0.0.1:8000/api/schema/swagger-ui/) to access the Swagger UI documentation.
