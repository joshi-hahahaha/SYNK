export type AuthData = {
  email: string;
  username?: string;
  password: string;
  confirmPassword?: string;
};

export type Event = {
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
