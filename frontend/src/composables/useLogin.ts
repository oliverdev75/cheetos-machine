import useApi from "./api";

export default function useLogin() 
{
    const tryToLogin = async (email: string) => {
        try {
            const api = useApi();
            const response = await api.post('/login', { email });

            api.setAuthToken(response.token);

            return response;
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
        }
    }

    return tryToLogin;
}
