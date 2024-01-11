<script setup>
    const { data, pending, error, refresh } = await useFetch('http://127.0.0.1:8000/todo/', {
        lazy: true,
        headers: { authorization: "Basic YWRtaW46YWRtaW4=" },
    })

</script>

<template>
    <h1>todo fetch</h1>
</template>