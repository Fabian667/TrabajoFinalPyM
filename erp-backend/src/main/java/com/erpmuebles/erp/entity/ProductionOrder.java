package com.erpmuebles.erp.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.util.List;

@Entity
@Table(name = "production_order")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ProductionOrder {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, unique = true)
    private String number;
    
    @Column(nullable = false)
    private LocalDate creationDate;
    
    private LocalDate startDate;
    
    private LocalDate endDate;
    
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private ProductionOrderStatus status;
    
    @ManyToOne
    @JoinColumn(name = "product_id", nullable = false)
    private Product product;
    
    @Column(nullable = false)
    private Integer quantity;
    
    @Column(columnDefinition = "TEXT")
    private String observations;
    
    @OneToMany(mappedBy = "productionOrder", cascade = CascadeType.ALL)
    private List<StageLog> stageLogs;
    
    @OneToMany(mappedBy = "productionOrder", cascade = CascadeType.ALL)
    private List<MaterialConsumption> materialConsumptions;
}
