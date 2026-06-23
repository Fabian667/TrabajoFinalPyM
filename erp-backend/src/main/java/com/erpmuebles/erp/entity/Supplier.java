package com.erpmuebles.erp.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Entity
@Table(name = "supplier")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Supplier {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    private String contact;
    
    private String email;
    
    private String phone;
    
    private String address;
    
    @OneToMany(mappedBy = "supplier", cascade = CascadeType.ALL)
    private List<RawMaterial> rawMaterials;
}
