import useApi from "./api";

export default function useLogin() {
    const tryToLogin = async (email: string, password: string) => {
        try {
            const api = useApi();
            const response = await api.post("/login", { email, password });
            api.setAuthToken(response.token);
            return response;
        } catch (error) {
            console.error("Error al iniciar sesión:", error);
        }
    };

    function getUserIdFromToken(token: string): number | null {
        try {
            const payloadBase64 = token.split('.')[1];
            // Algunos tokens usan base64url, hay que sustituir algunos caracteres:
            const payload = atob(payloadBase64.replace(/-/g, '+').replace(/_/g, '/'));
            const payloadObj = JSON.parse(payload);
            return payloadObj.user_id || null;
        } catch (e) {
            console.error("Error decoding token:", e);
            return null;
        }
    }

    return {
        getUserIdFromToken,
        tryToLogin
    };
}

