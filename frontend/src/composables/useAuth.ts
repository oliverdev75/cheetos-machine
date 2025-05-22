import useApi from "./api";

export default function useLogin() {
    const tryToLogin = async (email: string, password: string) => {
        try {
            const api = useApi();
            const response = await api.post("/login", { email, password });

            // Guarda el token
            localStorage.setItem("authToken", response.token);
            localStorage.setItem("authEmail", email);

            // Setea el token para futuras peticiones
            api.setAuthToken(response.token);
            console.log(response.token);
            return response;
        } catch (error) {
            console.error("Error al iniciar sesión:", error);
        }
    };

    const getUser = async () => {
        const api = useApi();

        const token = localStorage.getItem("authToken");
        if (!token) 
            return null;

        try {
            const email = localStorage.getItem("authEmail");
            console.log(email);
            
            // Quitar /api porque baseURL ya lo incluye
            const response = await api.get(`/user?email=${email}`);

            console.log(response);

            return response;
        } catch (e) {
            console.error("Error decoding token or fetching user:", e);
            return null;
        }
    };


    return {
        tryToLogin,
        getUser
    };
}
