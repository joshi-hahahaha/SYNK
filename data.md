# data.md

```js
// DATA MODEL
db: {
  users: [User.id],
  events: [Event.id],
}

// TYPES
type User = {
  id: string,
  photo:? string,
  firstname: string,
  lastname: string,
  username: string,
  email: string,
  password: hashed_password(string),
  reconfirmedpassword: string, 
  events: array<Event>,
}

type Event = {
  id: string,
  name: string,
  photo:? string,
  description: string,
  host: User.id,
  longitude: float,
  latitude: float,
  isPublic: boolean,
  startTime: integer (milliseconds),
  endTime: integer (milliseconds),

  // Optional if we get here
  rating:? integer,
}

```
