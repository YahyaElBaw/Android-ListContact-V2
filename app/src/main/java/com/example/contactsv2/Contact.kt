package com.example.contactsv2

import java.io.Serializable

/**
 * Modèle de données représentant un Contact pour la Version 2.
 */
data class Contact(
    val id: Long = 0,
    var nom: String,
    var prenom: String,
    var telephone: String,
    var email: String,
    var photoUri: String? = null
) : Serializable
