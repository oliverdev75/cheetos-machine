// src/composables/useOrders.ts
import Api from '../utils/Api'

export default function useOrders() {
    const api = Api.access()

    const getOrders = async () => {
        try {
            const res = await api.get('/order')
            return res
        } catch (err) {
            console.error("Error fetching orders:", err)
        }
    }

    const getOrder = async (id: number) => {
        try {
            const res = await api.get(`/order/${id}`)
            return res
        } catch (err) {
            console.error(`Error fetching order ${id}:`, err)
        }
    }

    const createOrder = async (user_id: number, price: number, products: number[]) => {
        try {
            const res = await api.post('/order', { user_id, price, products });
            return res.data;  // axios devuelve los datos en .data
        } catch (error: any) {
            // axios pone el error dentro de error.response.data si es respuesta del backend
            if (error.response && error.response.data && error.response.data.message) {
                throw new Error(`Error creating order: ${error.response.data.message}`);
            }
            throw new Error(`Error creating order: ${error.message || 'Unknown error'}`);
        }
    };


    const deleteOrder = async (id: number) => {
        try {
            const res = await api.del(`/order/${id}`)
            return res
        } catch (err) {
            console.error("Error deleting order:", err)
        }
    }

    const checkLastOrderDeliverDate = async (user_id: number) => {
        try {
            const res = await api.get(`/order/check?user_id=${user_id}`)
            console.log(res);
            return res;
        }
        catch (err) {
            console.error(err);
        }
    }

    const deliverLastOrder = async (user_id: number) => {
        try {
            const res = await api.post('/order/deliver', { user_id });
            return res.data;
        } catch (error: any) {
            if (error.response && error.response.data && error.response.data.message) {
                throw new Error(`Error delivering order: ${error.response.data.message}`);
            }
            throw new Error(`Error delivering order: ${error.message || 'Unknown error'}`);
        }
    };


    return {
        getOrders,
        getOrder,
        createOrder,
        deleteOrder,
        checkLastOrderDeliverDate,
        deliverLastOrder
    }
}
