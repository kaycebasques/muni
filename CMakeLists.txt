cmake_minimum_required(VERSION 3.13)
include(pico-sdk/external/pico_sdk_import.cmake)
project(app_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()
add_executable(app main.c)
pico_enable_stdio_usb(app 1)
pico_enable_stdio_uart(app 0)
pico_add_extra_outputs(app)

target_compile_definitions(app PRIVATE
        WIFI_SSID=\"${WIFI_SSID}\"
        WIFI_PASSWORD=\"${WIFI_PASSWORD}\"
        )
target_include_directories(app PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
        )
target_link_libraries(app
        pico_cyw43_arch_lwip_poll
        pico_lwip_mbedtls
        pico_mbedtls
        pico_stdlib
        hardware_i2c
        )

# Ignore warnings from lwip code
set_source_files_properties(
        ${PICO_LWIP_PATH}/src/apps/altcp_tls/altcp_tls_mbedtls.c
        PROPERTIES
        COMPILE_OPTIONS "-Wno-unused-result"
        )
