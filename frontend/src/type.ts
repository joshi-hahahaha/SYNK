export type AuthData = {
  email: string;
  username?: string;
  password: string;
  confirmPassword?: string;
};

export type EventObj = {
  id: string;
  ownerId: string;
  name: string;
  latitude: number;
  longitude: number;
  description: string;
  isPublic: boolean;
  start: string;
  end: string;
};

export type AuthRes = {
  message: string;
  token: string;
  userid: string;
};
