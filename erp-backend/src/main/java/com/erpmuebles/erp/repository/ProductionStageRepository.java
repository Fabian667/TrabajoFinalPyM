package com.erpmuebles.erp.repository;

import com.erpmuebles.erp.entity.ProductionStage;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductionStageRepository extends JpaRepository<ProductionStage, Long> {
}
