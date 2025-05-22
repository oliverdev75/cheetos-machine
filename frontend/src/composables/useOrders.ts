// src/composables/useOrders.ts
import useApi from './api'

export default function useOrders() {
    const api = useApi()

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

    const createOrder = async (userId: number, price: number, products: number[]) => {
        const res = await fetch('/api/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: userId,
                price: price,
                products: products
            })
        })
        return await res.json()
    }


    const deleteOrder = async (id: number) => {
        try {
            const res = await api.del(`/order/${id}`)
            return res
        } catch (err) {
            console.error("Error deleting order:", err)
        }
    }

    return {
        getOrders,
        getOrder,
        createOrder,
        deleteOrder
    }
}
